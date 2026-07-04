import shutil

# Get disk usage
total, used, free = shutil.disk_usage("/")

# Convert bytes to GB
total_gb = total // (1024 ** 3)
used_gb = used // (1024 ** 3)
free_gb = free // (1024 ** 3)

print("=" * 40)
print("      Linux Disk Usage Report")
print("=" * 40)
print(f"Total Space : {total_gb} GB")
print(f"Used Space  : {used_gb} GB")
print(f"Free Space  : {free_gb} GB")
print("=" * 40)
