void setup() {
  Serial.begin(115200);
}

void loop() {
  float temperatura = 25.0;
  float humedad = 60.0;
  int luz = 500;

  Serial.print(temperatura);
  Serial.print(",");
  Serial.print(humedad);
  Serial.print(",");
  Serial.println(luz);

  delay(2000);
}
