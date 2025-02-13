# **Driveline Baseball OBDB High Performance Assessment Documentation**

Our assessment process utilizes force plate tests paired with motion capture data to provide a comprehensive analysis of an athlete’s performance. This documentation outlines the key tests we use, their significance, and how we integrate the collected data

## **Testing Battery (Protocols included in links)-**

[**Table ROM and Shoulder Strength**](https://vimeo.com/382787527/9cf56a289c)**\-**  

The two datapoints included in the dataset are Thoracic spine mobility (measured on hands and knees) and supine shoulder internal and external rotation strength (measured with a dynamometer)

### [**Isometric Mid-Thigh Pull (IMTP)**](https://vimeo.com/972866323/3cc3060c4a)

The IMTP assesses lower body maximal strength by measuring the force an athlete can exert in a static position. This test is critical for understanding an athlete's raw strength and capacity to produce force, which is foundational for many athletic movements.

**Significance:**

* **Net Peak Force (Net PF):** Indicates absolute strength, or how much total force an athlete is capable of producing  
* **Relative Strength:** Shows strength in relation to bodyweight, useful for weight-class sports and performance optimization.

### [**Countermovement Jump (CMJ)**](https://vimeo.com/972660522/7656aa79fa)

The CMJ evaluates lower body explosive strength by measuring the athlete’s ability to generate power using a countermovement. It provides insights into an athlete’s vertical jump performance and overall power production.

**Significance:**

* **Jump Height:** Directly correlates with lower body power, a key indicator of athletic performance.  
* **Asymmetries:** Identifies imbalances between limbs, which can inform targeted training interventions.  
* **Rate of Force Development:** Assesses explosive power capabilities, important for sports requiring rapid movements.

### [**Squat Jump (SJ)**](https://vimeo.com/972826412/9daaa9c9cf)

The SJ measures lower body explosive strength from a static position, eliminating the stretch-shortening cycle. This test focuses on pure concentric power generation without the aid of pre-stretch.

**Significance:**

* **Peak Power:** Indicates the ability to generate maximal force quickly, essential for explosive activities.  
* **Jump Height:** Directly correlates with lower body power, a key indicator of athletic performance.  
* **Asymmetries:** Highlights discrepancies between limbs, useful for injury prevention and rehabilitation.  
* **Eccentric Utilization Ratio (EUR):** Compares CMJ to SJ height to evaluate an athlete’s ability to utilize the stretch-shortening cycle.

[**Plyo Pushup**](https://vimeo.com/991424293/9c27f2b889?share=copy) **(Not included in entire dataset)**

The plyo pushup measures upper body rate of force development using a countermovement.

**Significance:**

* **Peak Takeoff Force**\- the peak force achieved before the athlete's hands leave the plates  
* **Peak Eccentric Force**\- the peak force achieved during the eccentric phase of the plyo pushup  
* **Asymmetry**\- The difference in force production between the right and left arms

### [**Repeated Hop Test**](https://vimeo.com/manage/videos/972840700/05fb7485ca)

The repeated hop test assesses lower body reactive ability by measuring the athlete’s capacity to quickly transition from eccentric to concentric movements. 

**Significance:**

* **Reactive Strength Index (RSI):** Combines flight time and ground contact time to assess explosive efficiency.  
* **Ground Contact Time:** Measures how quickly an athlete can rebound, important for reactive sports.  
* **Flight Time:** Reflects the height of each hop, indicating power and endurance.

## **Basic Metrics Overview-** 

### **Asymmetry Metrics**

1. **Asymmetry**: A relative measurement of the difference between two-sided values expressed as a percentage. Calculated as (Left Metric value – Right Metric value) / maximum of (Left Metric value or Right Metric value) x 100\.

### **Force Metrics**

1. **Left Force**: The vertical Force component measured from the left force plate (N).  
2. **Right Force**: The vertical Force component measured from the right force plate (N).  
3. **Concentric Mean Force/BM**: Concentric Mean Force divided by Body Mass (N/kg).  
4. **Peak Force**: The highest force achieved in the movement  
5. **Net Peak Force**: The highest force achieved in the movement minus bodyweight

**Flight Time:** The total time from when an athlete's feet leave the plates to landing

### **Impulse Metrics**

1. **Concentric Impulse**: Net Impulse during the Concentric Phase (Ns).  
2. **Concentric Impulse (Abs) / BM**: Absolute Impulse during the Concentric Phase divided by Body Mass (Ns/kg).  
3. **Concentric Impulse-100ms**: Net Impulse during the first 100ms of the Concentric Phase (Ns).  
4. **Concentric Impulse-50ms**: Net Impulse during the first 50ms of the Concentric Phase (Ns).

### **Power Metrics**

1. **Concentric Mean Power**: Average Power during the Concentric Phase (W).  
2. **Concentric Mean Power / BM**: Concentric Mean Power divided by Body Mass (W/kg).  
3. **Peak Power**: Maximum Power during the Concentric Phase (W).  
4. **Peak Power / BM**: Peak Power divided by Body Mass (W/kg).

## **Metrics Naming Convention** ##

Most metrics in the dataset will follow the naming convention

`variable_[units]_type_testabbreviation`

Where `variable` is a short description of the metric, `[units]` is the unit of measure, `type` denotes the metric data type (typically a mean or max/best of several trials), and `testabbrevion` is an abbreviation of the test type.

Test abbreviations are as follows...

- CMJ = countermovement jump
- SJ = squat jump
- HT = hop test
- IMTP = isometric midthigh pull
- PP = plyo pushup
