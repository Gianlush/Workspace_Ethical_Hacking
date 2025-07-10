import json
import sys
import os

# Hex flag value to name database
database = {
    0x00000001: "CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT",
    0x00010000: "CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT_ALT_NAME",
    0x00400000: "CT_FLAG_SUBJECT_ALT_REQUIRE_DOMAIN_DNS",
    0x00800000: "CT_FLAG_SUBJECT_ALT_REQUIRE_SPN",
    0x01000000: "CT_FLAG_SUBJECT_ALT_REQUIRE_DIRECTORY_GUID",
    0x02000000: "CT_FLAG_SUBJECT_ALT_REQUIRE_UPN",
    0x04000000: "CT_FLAG_SUBJECT_ALT_REQUIRE_EMAIL",
    0x08000000: "CT_FLAG_SUBJECT_ALT_REQUIRE_DNS",
    0x10000000: "CT_FLAG_SUBJECT_REQUIRE_DNS_AS_CN",
    0x20000000: "CT_FLAG_SUBJECT_REQUIRE_EMAIL",
    0x40000000: "CT_FLAG_SUBJECT_REQUIRE_COMMON_NAME",
    0x80000000: "CT_FLAG_SUBJECT_REQUIRE_DIRECTORY_PATH",
    0x00000008: "CT_FLAG_OLD_CERT_SUPPLIES_SUBJECT_AND_ALT_NAME"
}

def replace_flags_recursive(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "Certificate Name Flag" and isinstance(value, list):
                obj[key] = [
                    database.get(int(v), f"UNKNOWN_FLAG_{v}") if isinstance(v, (int, str)) and str(v).isdigit() else f"INVALID_{v}"
                    for v in value
                ]
            else:
                replace_flags_recursive(value)
    elif isinstance(obj, list):
        for item in obj:
            replace_flags_recursive(item)

def load_file(path):
    with open(path, 'r') as f:
        content = f.read()
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        print("Error: File is not valid JSON.")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <file.json>")
        return

    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print("Error: File does not exist.")
        return

    data = load_file(filepath)
    replace_flags_recursive(data)
    with open(filepath, "w") as f:
        f.write(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()
