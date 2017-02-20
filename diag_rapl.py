import time
import rapl

if __name__ == "__main__":
	while True:
		s1 = rapl.RAPLMonitor.sample()
		time.sleep(1)
		s2 = rapl.RAPLMonitor.sample()

		diff = s2 - s1

		#s1e = s1.domains["package-0"].subdomains["core"].values["energy_uj"]
		s1e = s1.energy("package-0", "core")
		#s2e = s2.domains["package-0"].subdomains["core"].values["energy_uj"]
		s2e = s2.energy("package-0", "core")
		#diffe = diff.domains["package-0"].subdomains["core"].values["energy_uj"]
		diffe = diff.energy("package-0", "core")
		power = diff.average_power("package-0", "core")
	
		print "%d - %d = %d ----- (power=%0.2fW)" % (s2e, s1e, diffe, power)
