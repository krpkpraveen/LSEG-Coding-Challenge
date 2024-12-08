# LSEG-Coding-Challenge
## LSEG: Pre-Interview Coding Challenge

**Summary:**</br>
- Here’s a Python script that queries the metadata of an instance within Azure/AWS and outputs the data in JSON format.</br>
- Azure provides metadata about an instance through a well-defined metadata service available at http://instance-IP/metadata/instance.</br>

**Key Points:**
- Metadata API URL:</br>
        The metadata service is accessed at http://instance-IP/metadata/instance.</br>
        You must include the Metadata: true header in your request.</br>
- Query Parameters:</br>
        You can specify the api-version parameter to ensure compatibility with the API.</br>
- SON Formatting:</br>
        The script formats the output using Python's json.dumps function for readability.</br>
- Dependencies:</br>
        Install the requests library if not already available. Use pip install requests.</br>
- Running the Script:</br>
        This script is intended to be run within an Azure VM or environment with access to the metadata endpoint.</br>

## Bonus Points : The code allows for a particular data key to be retrieved individually
**Summary:** So that a specific data key from the Azure instance metadata can be retrieved individually, I have added functionality to allow the user to query a specific key.

**Key Parameter:**
  - The function get_azure_instance_metadata now accepts an optional parameter key which allows you to query a specific piece of metadata.</br>
  - If the key is provided, it retrieves the corresponding value for that key.</br>
  - If the key does not exist, it returns "Key not found in metadata".</br>

**Example Usage:**
  - To retrieve the full metadata, simply call get_azure_instance_metadata().</br>
  - To retrieve metadata for a specific key (like compute), call get_azure_instance_metadata("compute").</br>

**Example Outputs:**
</br>
![image](https://github.com/user-attachments/assets/71c1fe89-62d9-42b9-8737-56d536af2687)

**Specific Key ("compute"):**
</br>
![image](https://github.com/user-attachments/assets/8ca73e39-99a1-4fac-9706-65e872a9c173)
