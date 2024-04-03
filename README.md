## Actuator Endpoint Checker
Actuator Endpoint Checker is a command-line tool designed to check the accessibility of Actuator endpoints in web applications. Actuator endpoints provide insight into the internal state of a running application, making them valuable targets for pentesters to assess the security posture of an application.

## How it works
The tool takes a base URL and a wordlist file containing endpoint paths as input. It constructs URLs by appending each endpoint path from the wordlist to the base URL and then sends HTTP GET requests to check if the endpoints are accessible. If an endpoint returns a 200 OK status code, it is considered accessible and listed as a result.

## Features
- Efficiently checks the accessibility of Actuator endpoints.
- Supports custom base URLs and wordlist files for flexibility.
- Handles HTTP requests and responses with the `requests` library.
- Provides clear and concise output to identify accessible endpoints.

## How to use
1. **Clone the repository** to your local machine:

`git clone https://github.com/your-username/actuator-endpoint-checker.git`

2. **Navigate** to the directory containing the script:

`cd actuator-endpoint-checker`

3. **Run the tool** with the following command:

`python actuator.py -u <base_URL> -w <wordlist_file>`

Replace `<base_URL>` with the base URL of the web application you want to assess, and `<wordlist_file>` with the path to a wordlist file containing endpoint paths. 

For example:
`python actuator.py -u https://example.com -w wordlist.txt`

4. The tool will print the accessible Actuator endpoints found based on the combination of the base URL and endpoint paths in the wordlist file.
   
![image](https://github.com/MrLups/ActuatorEndpointChecker/assets/83069165/282bbf24-234b-45f5-9947-36edfc89a0e7)


## Why it's awesome for pentesters
- **Automates endpoint accessibility checks:** Instead of manually testing each endpoint, the tool automates the process, saving time and effort for pentesters.
- **Flexible and customizable:** Supports custom base URLs and wordlist files, allowing pentesters to tailor the assessment to the specific target application.
- **Clear and informative output:** Provides clear feedback on accessible endpoints, enabling pentesters to quickly identify potential attack vectors and security vulnerabilities.

