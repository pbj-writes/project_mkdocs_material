## Embed Content

I want the concept of a content reference or a reusable chunk of content that appears in multiple parts of my document. The use cases are myriad. Perhaps I want to repeat how to generate a token many times throughout my dev docs instead of creating a lot of links. Perhaps I have a great tutorial that I want to reuse. Or maybe I just want to have a consistent copyright statement or legal disclaimer across my docs.

### Example

Pointing the configuration (`mkdocs.yml`) to a directory with reusable content.

```yaml
plugins:
  - macros:
      include_dir: include
```

Content of the `include` directory.

``` { .sh .no-copy }
.
├─ include/
│  └─ embed_content.md
└─ mkdocs.yml
```

Adding the content reference inline.

```text
{{ "{% include 'embed_content.md' %}" }}
```

!!! check-work "Check My Work"

    Click the :material-eye: at the top of the page ⬆️