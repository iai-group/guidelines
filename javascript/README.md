# IAI Javascript Guidelines

  * Use Typescript
  * Use ES6 syntax
  * Use [eslint](https://eslint.org/) for linting
  * Use [prettier](https://prettier.io/) for formatting
  * Use [jest](https://jestjs.io/) for testing

## Bootstrap

  * While not mandatory, bootstrapping makes it easier to get started with a new project
    - Use [create-react-app](https://create-react-app.dev/) to bootstrap a new project
    - Use [react-bootstrap](https://react-bootstrap.github.io/) for UI components

## Development

    * Use [npm](https://www.npmjs.com/) to manage dependencies
    * Do not commit the `node_modules` directory to the repository

## Build

  * If using create-react-app, the build is already configured and you can simply run `npm run build` to build the project
  * Otherwise:
    - Use [webpack](https://webpack.js.org/) to build the project
    - Use [babel](https://babeljs.io/) to transpile the code
  * Do not commit the build output to the repository

## Release

  * Install release-it: `npm install --save-dev release-it`
    - release-it is a tool to automate the release process, including bumping the version, creating a git tag, and publishing the package to npm
