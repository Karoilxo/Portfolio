// przycisk
const int buttonPin = 7;              // pin przycisku
int buttonState = 0;                  // aktualny stan przycisku
int lastButtonState = 0;              // poprzedni stan przycisku

// serwo
#include <Servo.h>
Servo myservo;                        // obiekt serwa

// odbiornik IR
#include <IRremote.h>
const int RECV_PIN = 4;               // pin odbiornika IR

// wyświetlacz
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);   // adres i rozmiar wyświetlacza
int miejsca = 5;                      // liczba miejsc parkingowych

// diody
const int redLedPin = 2;              // pin czerwonej diody
const int greenLedPin = 3;            // pin zielonej diody

// kody pilota
unsigned long kodPilota = 0xE916FF00; // kod przycisku z pilota

void setup() {
  pinMode(redLedPin, OUTPUT);         // ustawienie pinu czerwonej diody jako wyjście
  pinMode(greenLedPin, OUTPUT);       // ustawienie pinu zielonej diody jako wyjście
  digitalWrite(redLedPin, HIGH);      // czerwona dioda włączona
  digitalWrite(greenLedPin, LOW);     // zielona dioda wyłączona

  pinMode(buttonPin, INPUT_PULLUP);   // przycisk z wewnętrznym rezystorem podciągającym

  myservo.attach(5);                  // serwo na pinie 5
  myservo.write(90);                  // szlaban w dół

  IrReceiver.begin(RECV_PIN, ENABLE_LED_FEEDBACK); // inicjalizacja odbiornika IR

  lcd.init();                         // inicjalizacja LCD
  lcd.backlight();                    // włączenie podświetlenia
  lcd.setCursor(0, 0);                // początek pierwszej linii
  lcd.print("Parking");               // tekst na LCD
  lcd.setCursor(0, 1);                // początek drugiej linii
  lcd.print("Ilosc miejsc: ");        // tekst na LCD
  lcd.print(miejsca);                 // wyświetlenie liczby miejsc

  Serial.begin(9600);                 // komunikacja szeregowa z PC
}

void loop() {
  buttonState = digitalRead(buttonPin);                           // odczyt stanu przycisku
  if (buttonState != lastButtonState && buttonState == LOW) {     // jeśli przycisk wciśnięty
    otworzSzlaban();                                              // otwarcie szlabanu
    miejsca = max(miejsca - 1, 0);                                // zmniejszenie liczby miejsc
    pokazMiejsca();                                               // aktualizacja LCD
    delay(50);                                                    // małe opóźnienie
  }
  lastButtonState = buttonState;                                  // zapamiętanie stanu przycisku

  if (IrReceiver.decode()) {                                      // sprawdzanie sygnału IR
    unsigned long sygnal = IrReceiver.decodedIRData.decodedRawData; // przypisanie zmiennej surowej wartości kodu przycisku
    Serial.print("Kod IR: 0x");                                   // wypisanie kodu
    Serial.println(sygnal, HEX);

    if (sygnal == kodPilota) {                                    // jeśli kod pasuje
      otworzSzlaban();                                            // otwarcie szlabanu
      miejsca = max(miejsca + 1, 0);                              // zwiększenie liczby miejsc
      pokazMiejsca();                                             // aktualizacja LCD
    }

    IrReceiver.resume();                                          // gotowość na kolejny sygnał
  }
}

// --- funkcje ---
void otworzSzlaban() {
  digitalWrite(redLedPin, LOW);                                   // czerwona dioda wyłączona
  digitalWrite(greenLedPin, HIGH);                                // zielona dioda włączona
  myservo.write(180);                                             // szlaban w górę
  delay(2500);                                                    // czas otwarcia
  digitalWrite(greenLedPin, LOW);                                 // zielona dioda wyłączona
  digitalWrite(redLedPin, HIGH);                                  // czerwona dioda włączona
  myservo.write(90);                                              // szlaban w dół
}

void pokazMiejsca() {
  lcd.setCursor(0, 1);                                            // początek drugiej linii
  lcd.print("Ilosc miejsc:   ");                                  // wyczyszczenie linii
  lcd.setCursor(14, 1);                                           // ostatnie dwie kolumny
  lcd.print(miejsca);                                             // wyświetlenie liczby miejsc
}
