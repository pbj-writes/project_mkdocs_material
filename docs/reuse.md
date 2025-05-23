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