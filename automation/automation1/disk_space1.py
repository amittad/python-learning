import shutil

total, used, free = shutil.disk_usage("/")

free_gb = free // (1024 ** 3)

print(f"Free Space: {free_gb} GB")

if free_gb < 20:
    print("WARNING: Disk space is running low!")
else:
    print("Disk space is healthy.")
