## Twilio OA

A function that validates the address and returns where to route the message to

The return value will be one of:
• For address strings with invalid formatting, return "INVALID ADDRESS"
• For valid E.164 format addresses, return "SMS"
• For other channels, return the provider string as "WHATSAPP", "WECHAT", or "MESSENGER"

Constraints
• The address will be a string petween 1 - 258 characters long E.164 numbers
• May optionally start with +'
• Will have up to 15 digits in length (not including the '+')
• Digits can be between 0-9. The first digit can never be 0.
• Other channel addresses
• No whitespace allowed
• The provider and identifier will always be
separated by one colon (provider):
(identifier}
• Valid providers are: whatsapp, wechat, and
messenger

    Input: +15555555555
    Output: SMS
    Input: 15555555555
    Output: SMS
    Input: +15555555555555555
    Output: INVALID_ADDRESS
    Input: whatsapp:15555555555
    Output: WHATSAPP
    Input: wechat:identifier:ghke83772
    Output: INVALID_ADDRESS
    Input: wechat:ghke83772
    Output: WECHAT
    Input: whatsapp:+15555555555
    Output: WHATSAPP
    Input: messenger: 15555555555
    Output: MESSENGER
    Input: messenger: +15555555555
    Output: MESSENGER
    Input: messenger: +15555555555555555

### Solution
```python
def check_e_164_number(number):
    return re.search("^\\+?[1-9](?:[0-9]?){0,14}$", number)


def check_valid_identifier(number):
    return re.search("^[0-9A-Za-z+\\-_@.]{1,248}", number)


def checkPrint(number):
    if check_e_164_number(number):
        return "SMS"
    else:
        str_split = number.split(':')
        if len(str_split) == 2:
            provider = str_split[0].upper()
            identifier = str_split[1]
            if check_e_164_number(identifier):
                return provider
            elif check_valid_identifier(identifier):
                return provider
    return "INVALID"


if __name__ == '__main__':
    text = "+15555555555"
    print(checkPrint(text))
```