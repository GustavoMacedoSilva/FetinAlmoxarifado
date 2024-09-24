#include <SPI.h>
#include <MFRC522.h>

#define SS 10
#define RST 9

MFRC522 sensor(SS, RST);   
 

 
char st[20];
 
void setup() 
{
  Serial.begin(9600);   
  SPI.begin();      
  sensor.PCD_Init();  
  Serial.println("Aproxime a Tag do leitor...");
  Serial.println();
  mensageminicial();
}
 
void loop() 
{
  // Look for new cards
  if ( ! sensor.PICC_IsNewCardPresent()) 
  {
    return;
  }
  // Select one of the cards
  if ( ! sensor.PICC_ReadCardSerial()) 
  {
    return;
  }
  Serial.print("ID  :");
  String conteudo= "";
  byte letra;
  for (byte i = 0; i < sensor.uid.size; i++) 
  {
     Serial.print(sensor.uid.uidByte[i] < 0x10 ? " 0" : " ");
     Serial.print(sensor.uid.uidByte[i], HEX);
     conteudo.concat(String(sensor.uid.uidByte[i] < 0x10 ? " 0" : " "));
     conteudo.concat(String(sensor.uid.uidByte[i], HEX));
  }
  Serial.println();
  Serial.print("Mensagem : ");
  conteudo.toUpperCase();
  if (conteudo.substring(1) == "D3 61 7F 13") //ID 1 - Chaveiro
  {
    Serial.println("CHAVEIRO");
    Serial.println();
    delay(3000);
    mensageminicial();
  }
 
  if (conteudo.substring(1) == "C3 EE C1 2F") //ID 2 - Cartao
  {
    Serial.println("CARTAO BRANCO");
    Serial.println();
    delay(3000);
    mensageminicial();
  }
  
} 
 
void mensageminicial()
{
 
  Serial.println(" Aproxime a Tag do leitor");  
  Serial.println();  
}
