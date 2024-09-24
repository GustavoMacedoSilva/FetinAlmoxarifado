#include <SPI.h>
#include <MFRC522.h>
#include <string.h>

#define SS_PIN 10
#define RST_PIN 9

#define IDLE 0
#define WRITE 1
#define READ 2

MFRC522 leitor(SS_PIN, RST_PIN); // cria o leitor identificando os pinos
MFRC522::MIFARE_Key key; // cria chave de acesso para as tags

unsigned char state = IDLE; // indicador de estado da maquina de estados
byte block = 4; // indica o bloco 4 de memoria da tag
String command; // armazena comando indicado
char writeBuffer[16]; // buffer de escrita 

void setup() {
  Serial.begin(9600); // inicia o serial
  SPI.begin(); // inicia o protocolo SPI
  leitor.PCD_Init(); // inicia o sensor
  for (byte i = 0; i < 6; i++) {
    key.keyByte[i] = 0xFF;  //Cria chave de acesso padrão definida pela MIFRAE
  }
  //Serial.println("Sistema Iniciado!"); // DEBUG
}

void loop() {
  switch(state) {
    case IDLE:
      command = Serial.readStringUntil('\n');
      command.trim();
      changeState(command);
      break;
    case WRITE:
      writeTag();
      break;
    case READ:
      readTag();
      break;
  }
}

void changeState(String str) {

  char *command = str.c_str();
  char *args;
  char *slicer;

  // garante que não fique executando comandos caso não tenha entrada no serial
  if (str.length() < 1)
    return;

  // Sepeara a string recebida em comando e argumento
  slicer = strtok(command, " ");
  command = slicer;
  slicer = strtok(NULL, " ");
  args = slicer;

  if (strcmp(command, "WRITE") == 0) {
    state = WRITE;
    // Copia a string de args e preenche o restante dos 16 bytes com null
    strcpy(writeBuffer,args);
    for(int i = strlen(args); i < 16; i++)
      writeBuffer[i] = NULL;
    //Serial.println("Modo de Escrita!"); // DEBUG
  }

  if (strcmp(command, "READ") == 0) {
    state = READ;
    //Serial.println("Modo de Leitura!"); // DEBUG
  }

}

void readTag() {
  // Procurando novas Tags
  if ( ! leitor.PICC_IsNewCardPresent()) 
  {
    return;
  }
  // Selecionando uma das tags
  if ( ! leitor.PICC_ReadCardSerial()) 
  {
    return;
  }
  // armazenar os dados lidos
  byte buffer[18];
  byte size = sizeof(buffer);
  authenticate(); // tenta se autenticar
  // le dados no bloco
  MFRC522::StatusCode status = leitor.MIFARE_Read(block, buffer, &size);
  
  if (status == MFRC522::STATUS_OK) {
    for (byte i = 0; i < 16; i++) {
      Serial.write(buffer[i]); // escreve os dados lidos
    }
    Serial.print('\0');
    state = IDLE;
    deAuthenticate();
  } else {
    state = IDLE;
    //Serial.println("Erro na leitura!"); // DEBUG
    //Serial.print("Erro na escrita: "); // DEBUG
    //Serial.println(leitor.GetStatusCodeName(status)); // DEBUG
    Serial.println(-1); // indica que ouve erro
    deAuthenticate();
  }
}

void writeTag() {
  // Procurando novas Tags
  if ( ! leitor.PICC_IsNewCardPresent()) 
  {
    return;
  }
  // Selecionando uma das tags
  if ( ! leitor.PICC_ReadCardSerial()) 
  {
    return;
  }
  //byte data[] = writeBuffer;
  authenticate(); // tenta se autenticar
  // Escreve no bloco 4 da tag
  MFRC522::StatusCode status = leitor.MIFARE_Write(block, writeBuffer, 16);

  if (status == MFRC522::STATUS_OK) {
    state = IDLE;
    Serial.println(1);
    deAuthenticate();
  } else {
    state = IDLE;
    //Serial.print("Erro na escrita!"); // DEBUG
    //Serial.print("Erro na escrita: "); // DEBUG
    //Serial.println(leitor.GetStatusCodeName(status)); // DEBUG
    Serial.println(-1);
    deAuthenticate();
  }

}

void authenticate() {

  // Autentica o bloco antes de ler
  byte status = leitor.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, block, &key, &(leitor.uid));
  if (status != MFRC522::STATUS_OK) {
      //Serial.print(F("Falha na autenticação: ")); // DEBUG
      //Serial.println(leitor.GetStatusCodeName(status)); // DEBUG
      return;
  }
}

void deAuthenticate() {
  // Finaliza a comunicação com a tag e desativa a autenticação
  leitor.PICC_HaltA();        // Desativa a tag
  leitor.PCD_StopCrypto1();   // Encerra a autenticação criptografada
}
