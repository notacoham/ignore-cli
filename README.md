<h1 align='center'>ignore-cli</h1>

<p align="center">
    <b>Create .gitignore files for any python project with one command</b>
</p>

<details>
<summary>Table of Contents</summary>
<br>

- [What and why](#what-and-why)
- [Installation](#installation)
- [Usage](#usage)

</details>

# What and why

If you're anything like me, you always find yourself asking the question:
`What file types go into a .gitignore?`
or
`Should I list that directory?`
or heaven forbid...
`How do I remove a commit with a secret key?`
<br>
Well your days of waiting are finally over! With `ignore-cli` you can generate a `.gitignore` file with a single command! `ignore-cli` scans your project, and generates a `.gitignore` file with only the necessary contents, so no bulky templates needed!

# Installation

Currently, the package is only here on github and for python projects via pip, but if there is enough interest, maybe you can look for it on homebrew someday!

<dl>
    <dt>Virtual environment setup and activation in project directory:</dt>
    <dd><code>python3 -m venv .venv</code></dd>
    <dd><code>source .venv/bin/activate </code></dd>
    <br>
    <dt>Install from Github in project:</dt>
    <dd><code>pip install git+https://github.com/notacoham/ignore-cli.git</code></dd>
</dl>

# Usage

**NOTE:** This package will work in projects without git, but for obvious reasons it is intended to be used in projects that have git initialized.

## Creating .gitignore

The `create` command is to be used in a fresh project that does not have a `.gitignore` file in it yet. It does this by walking through your project and adding any files or directories that should be included in your typical `.gitignore` and adding it into a file for you. It will only add file and directory patterns that exist in your project.

```sh
$ ignore create [target-directory]
```



## Add patterns

The `rescan` command is to be used in projects that already have a `.gitignore` file that was created by the `create` command. This will rescan your project, and add any newly added files that should be in your `.gitignore`

```sh
$ ignore rescan [target-directory] 
```

**NOTE:** # If used without a directory, the default will be the current directory

