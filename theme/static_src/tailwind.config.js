/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',
        '../../templates/**/*.html',
         '../../**/templates/**/*.html',

        '../jobs/**/*.py',
        '../secret/**/*.py',

        '../../jobs/**/*.py',
        '../../secret/**/*.py',

        '../../**/jobs/**/*.py',
        '../../**/secret/**/*.py',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        
        

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
       
        

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {

        },

        colors: {
            'myBlue': {
                '100': '#e4edfa',
                '200': '#c3daf4',
                '300': '#8ebbeb',
                '400': '#5299de',
                '500': '#2c7ccb',
                '600': '#1c5da6',
                '700': '#194d8b',
                '800': '#184374',
                '900': '#193861',
                '950': '#112440',
            },
            'myGreen': {
                '100': '#e8f0e8',
                '200': '#d1e1d1',
                '300': '#acc9ac',
                '400': '#82a880',
                '500': '#588157',
                '600': '#4a7049',
                '700': '#3c593c',
                '800': '#334833',
                '900': '#2b3c2b',
                '950': '#141f15',
            },
            'myWhite': {
                '50': '#ffffff',
                '100': '#efefef',
                '200': '#dcdcdc',
                '300': '#bdbdbd',
                '400': '#989898',
                '500': '#7c7c7c',
                '600': '#656565',
                '700': '#525252',
                '800': '#464646',
                '900': '#3d3d3d',
                '950': '#292929',
            },
            'myRed': {
                '100': '#ffe3df',
                '200': '#ffcbc5',
                '300': '#ffa89d',
                '400': '#ff7665',
                '500': '#fe4b35',
                '600': '#ed341d',
                '700': '#c7220e',
                '800': '#a42010',
                '900': '#882114',
                '950': '#4a0d05',
            },
        },

    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}}
