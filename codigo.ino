int pinoNoRC=0; 
int valorLido = 0;
float tensaoCapacitor = 0, tensaoResistor;
unsigned long time; 
int buzzerPin=4;

void setup(){ 
  pinMode(buzzerPin,OUTPUT);
Serial.begin(9600); 
} 

void loop() {
  
	time=millis(); 
	valorLido=analogRead(pinoNoRC);
  	Serial.print(valorLido);
	tensaoResistor=(valorLido*5.0/1023); // 5.0V / 1023 degraus = 0.0048876 
	tensaoCapacitor = abs(5.0-tensaoResistor);
  if(tensaoCapacitor==5){
    digitalWrite(buzzerPin,HIGH);
  }
 	Serial.print(time); // imprime o tempo no MONITOR SERIAL
    Serial.print(" "); 
  	Serial.print(tensaoCapacitor);
  	Serial.print(" ");
  	Serial.println(tensaoResistor);
  	delay(400);
	
  
}