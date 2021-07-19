# VSCode

Our prefered IDE for python is [Visual Studio Code](https://code.visualstudio.com/).

## Installation

To download and install VSCode on macOS follow the instructions [here](https://code.visualstudio.com/docs/setup/mac).

## User interface

The layout image and information is taken from [this](https://code.visualstudio.com/docs/getstarted/userinterface) page where you can read about the user interface in more detail.

### Layout

![Layout](./figures/layout.png)

The UI is divided into five areas:

 - Editor - The main area to edit your files. You can open as many editors as you like side by side vertically and horizontally.
  - Side Bar - Contains different views like the Explorer to assist you while working on your project.
 - Status Bar - Information about the opened project and the files you edit.
 - Activity Bar - Located on the far left-hand side, this lets you switch between views and gives you additional context-specific indicators, like the number of outgoing changes when Git is enabled.
 - Panels - You can display different panels below the editor region for output or debug information, errors and warnings, or an integrated terminal. Panel can also be moved to the right for more vertical space.

### Command Palette

Command palette (`Cmd+Shift+P` or `F1`) is where you can find all available (both core and extensions) commands in VSCode. It acts as a search so you can simply type keywords of the command you want to use.

For example, if we want to access the json version of settings we simply type `settings json`. The third entry is for the global settings, and it is the one we use for configuration.

<!-- ![Settings](./figures/settings.png?s=600) -->
<img src="./figures/settings.png" width="600">


## Configuration


### Extensions

The strength and flexibility of VSCode are in the use of extensions. These are add-ons that unlock more features. The following are three lists of extensions; *Required*, *Recommended*, and *Suggested*. There are many more useful extensions not covered in this document.

**Required**
 - Python

**Recommended**
 - Python Docstring Generator
 - Python Test Explorer

**Suggested**
 - Remote - SSH
 - Latex Workshop
 - Todo Tree
 - Code Spell Checker
 - GitLens
 - GitHub Pull Requests and Issues

### Settings

Settings can be configured using UI or modifying the settings (JSON) file. Here we show the latter. 

**General and python extension**

```json
{
    "terminal.integrated.inheritEnv": false,
    "editor.rulers": [80, 120],
    "editor.formatOnSave": true,
    "python.formatting.provider": "black",
    "python.linting.flake8Enabled": true,
}
```

**Python Test Explorer**

```json
{
    "pythonTestExplorer.testFramework": "pytest",
}
```