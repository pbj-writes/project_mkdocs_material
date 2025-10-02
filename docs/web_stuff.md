---
status: new
---
# Advanced Features

Demonstrating some advanced features for specific use cases.

## UX and Doc Content Alignment

A design system may include protocols for externalizing UI strings. In a tightly coupled content strategy, you may want use these strings in your documentation as well.

In this example, strings are externalized in a JSON file and the Macros plugin extends out to do the rest. 

```json
{ 
    "locale": "en-US", 
    "translations": { 
        "user.table.name": "Name", 
        "user.table.address": "Address",
        "user.table.email": "Email",
        "user.table.username": "Username"
    } 
}
```

In the UI, imagine a user table where teammates can see each other's information on a user table.

In the documentation, the user table needs some conceptual and reference explanation.

### User Table

| Element | Description | Editable |
|---------|-------------|----------|
| {{ t("user.table.name") }} | The user first and last name. | ✅ |
| {{ t("user.table.location") }} | The user city and state. | ✅ |
| {{ t("user.table.email") }} | The user email address and unique identifier. Request an email change from your admin. | ❌ |
| {{ t("user.table.username") }} | The user selected display name. | ✅ |

!!! check-work "Check My Work"

    Click the :material-eye: at the top of the page ⬆️
