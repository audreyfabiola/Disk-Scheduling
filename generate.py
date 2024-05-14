import random

def generate_requests(file_name, num_requests, max_cylinder):
    with open(file_name, 'w') as file:
        for _ in range(num_requests):
            request = random.randint(0, max_cylinder - 1)
            file.write(str(request) + '\n')

if __name__ == "__main__":
    file_name = "cylinder_requests.txt"
    num_requests = 1000
    max_cylinder = 5000
    generate_requests(file_name, num_requests, max_cylinder)
    print(f"Generated {num_requests} random cylinder requests in file '{file_name}'")
