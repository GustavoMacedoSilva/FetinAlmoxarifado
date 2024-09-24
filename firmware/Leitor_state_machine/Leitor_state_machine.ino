#include <SPI.h>
#include <MFRC522.h>
#include <string.h>

#define SS_PIN 10
#define RST_PIN 9

#define IDLE 0
#define WRITE 1
#define READ 2

MFRC522 leitor(SS_PIN, RST_PIN); // cria o leitor identificando os pinos
MFRC522::MIFARE_Key key;

unsigned char state = IDLE;
byte block = 4; // indica o bloco 4 de memoria da tag
char command[50];

void setup() {
  Serial.begin(9600); // inicia o serial
  SPI.begin(); // inicia o protocolo SPI
  leitor.PCD_Init(); // inicia o sensor
  for (byte i = 0; i < 6; i++) {
    key.keyByte[i] = 0xFF;  //Cria chave de acesso padrão definida pela MIFRAE
  }
  Serial.println("Sistema Iniciado!");
}

void loop() {
  switch(state) {
    case IDLE:
      command = Serial.readStringUntil('\n');
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

  char command[] = str.c_str();
  char args[20];
  int i = 0;

  // encontra o indice do separador da string
  while(command[i] != ' ') {
    i++;
  }

  if (command == '1') {
    state = WRITE;
    Serial.println("Modo de Escrita!");
  }

  if (command == '2') {
    state = READ;
    Serial.println("Modo de Leitura!");
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

  byte data[] = "Bora Bill!";
  authenticate(); // tenta se autenticar
  // Escreve no bloco 4 da tag
  MFRC522::StatusCode status = leitor.MIFARE_Write(block, data, 16);

  if (status == MFRC522::STATUS_OK) {
    state = IDLE;
    Serial.println("Dados gravados com sucesso!");
    deAuthenticate();
  } else {
    state = IDLE;
    Serial.print("Erro na escrita!");
    Serial.print("Erro na leitura: ");
    Serial.println(leitor.GetStatusCodeName(status));
    deAuthenticate();
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
    Serial.println();
    state = IDLE;
    deAuthenticate();
  } else {
    state = IDLE;
    Serial.println("Erro na leitura!");
    Serial.print("Erro na escrita: ");
    Serial.println(leitor.GetStatusCodeName(status));
    deAuthenticate();
  }
}

void authenticate() {

  // Autentica o bloco antes de ler
  byte status = leitor.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, block, &key, &(leitor.uid));
  if (status != MFRC522::STATUS_OK) {
      Serial.print(F("Falha na autenticação: "));
      Serial.println(leitor.GetStatusCodeName(status));
      return;
  }
}

void deAuthenticate() {
  // Finaliza a comunicação com a tag e desativa a autenticação
  leitor.PICC_HaltA();        // Desativa a tag
  leitor.PCD_StopCrypto1();   // Encerra a autenticação criptografada
}