import numpy as np

np.random.seed(43)
temp = np.random.uniform(30, 50, size=(168))
vib = np.random.uniform(2, 6, size=(168))
rpm = np.random.randint(2850, 3500, size=(168))

r_temp = np.reshape(temp, shape=(7, 24))
r_vib = np.reshape(vib, shape=(7, 24))
r_rpm = np.reshape(rpm, shape=(7, 24))

daily_avg_temp = np.mean(r_temp, axis=1)
daily_avg_vib = np.mean(r_vib, axis=1)
daily_avg_rpm = np.mean(r_rpm, axis=1)

# test = [np.mean(i) for i in r_temp]
def inject_faults(signal, fault):
    new_signal = signal.copy()
    for key, value in fault.items():
        new_signal[key-1, np.random.randint(0, len(signal[key-1]))] = value
    return new_signal

fault_temp = inject_faults(r_temp, {3: 70, 6: 90})
fault_rpm = inject_faults(r_rpm, {3: 1000, 6: 5000})
fault_vib = inject_faults(r_vib, {3: 10, 6: 12})

new_temp = fault_temp.flatten()
new_rpm = fault_rpm.flatten()
new_vib = fault_vib.flatten()

std_temp = np.abs((new_temp - np.mean(new_temp))/ np.std(new_temp))
std_rpm = np.abs((new_rpm - np.mean(new_rpm))/ np.std(new_rpm))
std_vib = np.abs((new_vib - np.mean(new_vib))/ np.std(new_vib))

std_temp = np.reshape(std_temp, shape=(7, 24))
std_rpm = np.reshape(std_rpm, shape=(7, 24))
std_vib = np.reshape(std_vib, shape=(7, 24))

def outliers(signal):
    out = []
    #Iterating through the std to get the days and the values
    for pos, value in enumerate(signal):
        #Iterating through the days and getting the values and position
        for i, j in enumerate(value):
            if j > 3:
                #Appending the positons( days and inner positions) so they can be referenced later
                out.append([pos, i])
    return out

out_tmp = outliers(std_temp)
out_rpm = outliers(std_rpm)
out_vib = outliers(std_vib)

def print_outliers(out, parameter, signal):
    print(f"The outliers for {parameter} are: ")
    for i, j in out:
        print(f"Day {i+1}, value of {signal[i, j]}")
        
def highest_days(signal):
    highest = np.max(signal, axis=1)
    day = np.argmax(highest)
    return day

print_outliers(out_tmp, "temperature", fault_temp)
print_outliers(out_rpm, "RPM", fault_rpm)
print_outliers(out_vib, "vibration", fault_vib)

temp_day = highest_days(fault_temp)
vib_day = highest_days(fault_vib)
print(f"Highest temp days: {temp_day+1}")
print(f"Highest vibration days: {vib_day+1}")