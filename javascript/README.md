# IAI Javascript Guidelines

  * Use Typescript
  * Use ES6 syntax
  * Use [eslint](https://eslint.org/) for linting
  * Use [prettier](https://prettier.io/) for formatting
  * Use [jest](https://jestjs.io/) for testing
  * Highly recommended: Use [react](https://reactjs.org/) for UI development

## Bootstrap

  * While not mandatory, bootstrapping makes it easier to get started with a new project
    - Use [create-react-app](https://create-react-app.dev/) to bootstrap a new project
    - Use [react-bootstrap](https://react-bootstrap.github.io/) for UI components

## Development

    * Use [npm](https://www.npmjs.com/) to manage dependencies
    * Do not commit the `node_modules` directory to the repository, add it to the `.gitignore` file.

## Build

  * When building a project, the output should be placed in a `dist` or `build` directory.
    - This is to avoid confusion with the source code
  * The build output should be a single javascript file, or a set of files that can be easily included in a web page.
  * If using create-react-app, the build is already configured and you can simply run `npm run build` to build the project
  * Otherwise:
    - Use [webpack](https://webpack.js.org/) to build the project
    - Use [babel](https://babeljs.io/) to transpile the code
  * Do not commit the build output to the repository, add it to the `.gitignore` file.

## Release to GitHub and npm

  * When releasing a project, the source code should be published to GitHub, and the build output should be published to npm.
  * To simplify the process, install release-it: `npm install --save-dev release-it`
    - release-it is a tool to automate the release process, including bumping the version, creating a git tag, and publishing the package to npm
