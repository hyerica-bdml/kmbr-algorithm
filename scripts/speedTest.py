import subprocess, os


def run(k, num_of_points, num_of_iters):
    os.environ["K"] = f"{k}"
    os.environ["NUM_OF_POINTS"] = f"{num_of_points}"
    os.environ["NUM_OF_ITERATIONS"] = f"{num_of_iters}"
    # os.environ["NUM_OF_GROUPS"] = f"{max(int(num_of_points / 10), 10)}"
    os.environ["NUM_OF_GROUPS"] = f"{max(int(num_of_points / 1000), 10)}"
    os.environ["LOG_FILE"] = "logs/ours/log.txt"
    os.environ["NUM_DYNAMIC_ITERATIONS"] = "30"
    os.environ["MIN_MOVE"] = f"{max(50, int(num_of_points * 0.0005))}"
    os.environ["MAX_MOVE"] = f"{max(100, int(num_of_points * 0.001))}"
    # os.environ["MIN_MOVE"] = "50"
    # os.environ["MAX_MOVE"] = "100"
    os.environ["RUN_ON_DYNAMIC"] = "true"

    subprocess.run(["mvn", "clean", "compile", "exec:java", "-D", "exec.mainClass=edu.hanyang.kmbr.SpeedTestApp"])


if __name__ == "__main__":
    run(15, 1000000, 3)
    for k in range(5, 31, 5):
        for num_of_points in [10000, 50000, 100000, 500000, 1000000]:
            run(k, num_of_points, 3)
