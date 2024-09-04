#include <SPI.h>

void setup() {
  Serial.begin(9600);
  SPI.begin();
  SPI.setClockDivider(SPI_CLOCK_DIV8); // Configura o divisor de clock (por exemplo, para 2MHz)

  // Configura o pino de SS (Slave Select) como saída e o inicializa como HIGH
  pinMode(10, OUTPUT);
  digitalWrite(10, HIGH);

  Serial.println("Iniciando teste SPI...");
}

void loop() {
  digitalWrite(10, LOW); // Seleciona o dispositivo SPI
  byte response = SPI.transfer(0xAA); // Envia um byte (0xAA) e recebe o que o escravo enviar de volta
  digitalWrite(10, HIGH); // Deselecta o dispositivo SPI

  Serial.print("Resposta SPI: 0x");
  Serial.println(response, HEX);
  
  delay(1000); // Aguarda 1 segundo
}
