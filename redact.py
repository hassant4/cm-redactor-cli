import re, yaml, sys

class Redactor:

    def __init__(self, filepath='./rules.yml', replacement_string='[redacted]'):
        self.filepath = filepath
        self.rules = self.read_rules()
        self.replacement_string = replacement_string

    def read_rules(self):
        rules = {}
        with open(self.filepath) as rule_file:
            raw_rules = yaml.load(rule_file)

        for rule in raw_rules['Rules']:
            rules.update(rule)

        return rules

    def combine_rules(self):
        return '|'.join(self.rules.values())

    def apply_rule(self, string: str, rule_name: str):
        redacted = re.sub(self.rules[rule_name], self.replacement_string, string)
        return redacted

    def apply_rules(self, string: str): #applied in the order declared in dict, important for phone_number/zipcode interference 
        redacted = re.sub(self.combine_rules(), self.replacement_string, string)
        return redacted

if __name__ == '__main__':
    redactor = Redactor()
    if(len(sys.argv)>2):
        redacted = redactor.apply_rule(sys.argv[1], sys.argv[2])
    else:
        redacted = redactor.apply_rules(sys.argv[1])
    
    print(redacted)
