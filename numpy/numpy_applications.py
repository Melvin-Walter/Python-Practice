import numpy as np

np.random.seed(43)

temp = np.random.uniform(30, 90, size=100)
rpm = np.random.randint(2850, 3000, size=100)
vib = np.random.uniform(1.0, 5.0, size=100)
def compute_values(signal):
    mean = np.mean(signal)
    std = np.std(signal)
    max = np.max(signal)
    min = np.min(signal)
    
    stats = {
        "Mean": mean,
        "STD": std,
        "Max": max,
        "Min": min
    }
    return stats

temp_stats = compute_values(temp)
vib_stats = compute_values(vib)
rpm_stats = compute_values(rpm)


temp_filter = temp[temp > 80]
rpm_filter = rpm[rpm > 2500]
vib_filter = vib[vib > 4]

reshape_temp = temp.reshape(10, 10)
reshape_vib = vib.reshape(10, 10)
reshape_rpm = rpm.reshape(10, 10)

avg_temp = np.mean(reshape_temp, axis=1)
avg_vib = np.mean(reshape_vib, axis=1)
avg_rpm = np.mean(reshape_rpm, axis = 1)

temp_add = np.append(reshape_temp, np.random.uniform(100, 120, size=(1, 10)), axis=0)
vib_add = np.append(reshape_vib, np.random.uniform(6, 10, size=(1, 10)), axis=0)
rpm_add = np.append(reshape_rpm, np.random.randint(4000, 5000, size=(1, 10)), axis=0)

mean_list = []
for i in [temp_add, vib_add, rpm_add]:
    highest_mean = 0
    position = 0
    for pos, value in enumerate(i):
        current_mean = np.mean(value)
        if np.abs(current_mean) > highest_mean:
            highest_mean = current_mean
            position = pos
    mean_list.append([highest_mean, position+1])

temp = temp_add.flatten()
vib = vib_add.flatten()
rpm = rpm_add.flatten()
i = 0
while i < 3:
    g = np.random.randint(0, len(temp)+1, size=5)
    bad_temp = np.random.uniform(150, 200, size=1)
    bad_vib = np.random.uniform(11, 20, size=1)
    bad_rpm = np.random.uniform(1000, 2000, size=1)
    temp = np.insert(temp, g, bad_temp)
    vib = np.insert(vib, g, bad_vib)
    rpm = np.insert(rpm, g, bad_rpm)
    i += 1

def calculate_deviations(signal, mean , std):
    outliers = []
    for index, value in enumerate(signal):
        deviation = (value - mean) / std
        if np.abs(deviation) > 3:
            outliers.append([index, value])
    return outliers    

def scale(signal):
    min_values = np.min(signal)
    max_values = np.max(signal)
    return (signal - min_values)/(max_values - min_values)    

scaled_temp = scale(temp)
scaled_vib = scale(vib)
scaled_rpm = scale(rpm)

dev_temp = calculate_deviations(temp, temp_stats["Mean"], temp_stats["STD"])
dev_vib = calculate_deviations(vib, vib_stats["Mean"], vib_stats["STD"])
dev_rpm = calculate_deviations(rpm, rpm_stats["Mean"], rpm_stats["STD"])

print(f"Amount of anomalous temp {len(dev_temp)}")
print(f"Amount of anomalous rpm {len(dev_rpm)}")
print(f"Amount of anomalous vibration {len(dev_vib)}")
