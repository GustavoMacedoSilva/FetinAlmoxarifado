#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9

MFRC522 rfid(SS_PIN, RST_PIN); // Create MFRC522 instance

void setup() {
  Serial.begin(9600);   // Inicia a comunicação serial
  SPI.begin();          // Inicia a comunicação SPI
  rfid.PCD_Init();      // Inicia o leitor RC522
  Serial.println("Aproxime uma tag RFID do leitor...");
}

void loop() {
  // Verifica se existe uma nova tag presente
  if ( ! rfid.PICC_IsNewCardPresent()) {
    return;
  }

  // Verifica se a tag pode ser lida
  if ( ! rfid.PICC_ReadCardSerial()) {
    return;
  }

  // Imprime o UID da tag (identificação única)
  Serial.print("UID da tag:");
  for (byte i = 0; i < rfid.uid.size; i++) {
    Serial.print(rfid.uid.uidByte[i] < 0x10 ? " 0" : " ");
    Serial.print(rfid.uid.uidByte[i], HEX);
  }
  Serial.println();

  // Detalhes adicionais sobre a tag podem ser obtidos aqui

  // Pára de escanear esta tag (necessário para que o leitor possa detectar novas tags)
  rfid.PICC_HaltA();
}
