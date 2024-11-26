const int ldrPin = A5; // Pino onde o LDR está conectado
const int ledPin = 9;  // Pino onde o LED está conectado
const int pinoSensorSom = A0; // PINO ANALÓGICO UTILIZADO PELO SENSOR
int limite_som = 525; // Valor coletado a partir da calibração do sensor de som
int sensor_som = 0;
int intensidade_som = 0;
String sinais;


void setup() {
  Serial.begin(9600);      // Inicializa a comunicação serial
  delay(6000);
  pinMode(ledPin, OUTPUT); // Configura o pino do LED como saída
  pinMode(pinoSensorSom, INPUT); // DEFINE O PINO COMO ENTRADA
  
}

void loop() {
  // Lê o valor do LDR (0 a 1023)
  int lightValue = analogRead(ldrPin);
  // Mapeia o valor da luz para o brilho do LED (0 a 255)
  int ledBrightness = map(lightValue, 0, 1023, 255, 0);

  // Lê o valor do sensor de som
  int sensor_som = analogRead(pinoSensorSom);
  // Mede a intensidade do som, subtraindo o valor limite do som ao zero com o captado
  int intensidade_som = abs(sensor_som - limite_som);

  // Reunie todos os valores captados para exibição
  sinais = String(lightValue) + "|" + String(ledBrightness) + "|" + String(sensor_som) + "|" + String(intensidade_som);
  Serial.println(sinais);
  delay(1000);

}



