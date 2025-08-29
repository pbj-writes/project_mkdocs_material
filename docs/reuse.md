# {{ header1 }}

I'm demonstrating variables and content references that could apply at various levels of the document (local) or organization documents (suite or global).

I'm using the [`mkdocs-macros`](https://mkdocs-macros-plugin.readthedocs.io/en/latest/) plugin. This plugin enables several reuse use cases.

## Product Name (Singular)

I'll make up a product. I'll call it, {{ productName }}.

{{ productName }} makes delicious sandwiches.

Did you know that I've been using a variable for {{ productName }}? I'll show you.

In the case of a situation where you only have to talk about a single product, you can define the product name variable in your `mkdocs.yml` and then insert throughout your documentation.

### Example

Definition of the variable in the `mkdocs.yml`.

```yaml
extra:
  productName: pbjStand
```

Use of the variable on this page.

```text
I'll make up a product. I'll call it, {{ "{{ productName }}" }}.
```

!!! check-work "Check My Work"

    Click the :material-eye: at the top of the page ⬆️

## Product Names (Multiple)

Now, I have two (or more) products. I'll call them:

- {{ productName1 }}
- {{ productName2 }}

Instead of packing potentially dozens of product names into the `mkdocs.yml`, I can create a variable library, `product_names.yaml`. Externalizing variables into a library file helps keep your `mkdocs.yml` tight while having a one-stop for variables. I could also create more library files for other kinds of variables such as approved terminology or organization variables. Depending on the complexity of your docs, you might even have these libraries external to your doc repo and you pull them into your CI/CD workflows.

### Example

Definition of the variables in the variable library.

```yaml
#product_names.yaml

productName1: "Carrot Cake Donut"
productName2: "Cheesecake Donut"
```

Pointing the configuration (`mkdocs.yml`) to the content library.

```yaml
plugins:
  - macros:
      include_yaml:
        - product_names.yaml
```

Use of the variable on this page.

```text
Now, I have two (or more) products. I'll call them:

- {{ "{{ productName1 }}" }}
- {{ "{{ productName2 }}" }}
```

!!! check-work "Check My Work"

    Click the :material-eye: at the top of the page ⬆️

{% include 'embed_content.md' %}

## Reuse Content from Another Repo

This is not magic. In my GitHub workflow file, I pull in the content from another repo and copy it into the contents of my main repo build process so that all relevant content is available during the site build.

### Example

In this case, I'm pulling in all the content from my [`content_lib`](https://github.com/pbj-writes/content_lib) repo.

The `content_lib` repo contains a variable library file ([`var_lib.yaml`](https://github.com/pbj-writes/content_lib/blob/main/var_lib.yaml)). The `var_lib.yaml` file contains two variable key-value pairs.

```yaml
#var_lib.yaml

productName3: "PBJ's Writing Service"
productName4: "PBJ's Bike Shop"
```

Below 👇, I have two variables that are NOT defined in the contained repo, `project_mkdocs_material`. Again, these variables are defined in the [`content_lib`](https://github.com/pbj-writes/content_lib) repo.

{{ productName3 }}

{{ productName4 }}

!!! check-work "Check My Work"

    Click the :material-eye: at the top of the page ⬆️

## Conditions

Perhaps you want to show or hide content in certain contexts like for certain user types or deployment types.

### Audience

{% if audience == "user" %}
This is user content.
{% elif audience == "dev" %}
This is developer content.
{% endif %}

{% raw %}
```jinja2
{% if audience == "user" %}
This is user content.
{% elif audience == "dev" %}
This is developer content.
{% endif %}
```
{% endraw %}

!!! check-work "Check My Work"

    Click the :material-eye: at the top of the page ⬆️
