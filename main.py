import dht
from machine import Pin
import time

# DHT22 Sensor
sensor = dht.DHT22(Pin(13))

# LED Bargraph
bargraph_pins = [0, 4, 16, 17, 5, 18, 19, 21, 22, 23]
leds = [Pin(pin, Pin.OUT) for pin in bargraph_pins]

# Buzzer
buzzer = Pin(14, Pin.OUT)

# Enhanced Simple LCD implementation
class SimpleLCD:
    def __init__(self, rs, en, d4, d5, d6, d7):
        self.rs = rs
        self.en = en
        self.data_pins = [d4, d5, d6, d7]
        self.all_pins = [rs, en] + self.data_pins
        
        # Initialize all pins
        for pin in self.all_pins:
            pin.init(Pin.OUT)
            pin.value(0)
        
        time.sleep_ms(20)  # LCD power-up delay
        self.init_lcd()
    
    def init_lcd(self):
        # Initialization sequence
        self.cmd(0x33)
        time.sleep_ms(5)
        self.cmd(0x32)
        time.sleep_ms(5)
        self.cmd(0x28)  # 4-bit mode, 2-line, 5x8 font
        time.sleep_ms(5)
        self.cmd(0x0C)  # Display on, cursor off
        self.cmd(0x06)  # Increment cursor
        self.clear()
    
    def cmd(self, byte):
        self.rs(0)
        self.write_nibble(byte >> 4)
        self.write_nibble(byte & 0x0F)
        if byte in (0x01, 0x02):  # Clear or home command
            time.sleep_ms(2)
    
    def write_nibble(self, nibble):
        for i in range(4):
            self.data_pins[i].value((nibble >> i) & 1)
        self.pulse_en()
    
    def pulse_en(self):
        self.en(0)
        time.sleep_us(1)
        self.en(1)
        time.sleep_us(1)
        self.en(0)
        time.sleep_us(100)
    
    def clear(self):
        self.cmd(0x01)
        time.sleep_ms(2)
    
    def write(self, x, y, text):
        addr = 0x80 + (0x40 * y) + x
        self.cmd(addr)
        self.rs(1)
        for char in text:
            self.write_nibble(ord(char) >> 4)
            self.write_nibble(ord(char) & 0x0F)
            time.sleep_us(50)

# Initialize LCD with recommended pins
try:
    lcd = SimpleLCD(
        Pin(25), Pin(26),  # RS, EN
        Pin(27), Pin(12), Pin(15), Pin(2)  # D4-D7
    )
    lcd_available = True
except Exception as e:
    print("LCD initialization failed:", e)
    lcd_available = False

def afficher_bargraph(temp):
    max_temp = 50
    num_leds_on = min(max(int((temp/max_temp)*len(leds)), 0), len(leds))
    for i in range(len(leds)):
        leds[i].value(1 if i < num_leds_on else 0)

def afficher_lcd(temp):
    if lcd_available:
        try:
            lcd.clear()
            lcd.write(0, 0, f"Temp: {temp:.1f} C")
            if temp >= 35:
                lcd.write(0, 1, "ALERTE TEMP ELEVEE!")
        except Exception as e:
            print("LCD Error:", e)
    print(f"Temperature: {temp:.1f} C" + (" (ALERT!)" if temp >= 35 else ""))

def control_buzzer(temp):
    buzzer.value(1 if temp >= 35 else 0)

def main():
    while True:
        try:
            sensor.measure()
            temp = sensor.temperature()
            
            afficher_bargraph(temp)
            afficher_lcd(temp)
            control_buzzer(temp)
            
        except OSError as e:
            print("DHT Error:", e)
            if lcd_available:
                lcd.clear()
                lcd.write(0, 0, "Erreur Capteur")
            time.sleep(1)
            continue
        except Exception as e:
            print("Unexpected error:", e)
        
        time.sleep(2)

if __name__ == "__main__":
    main()