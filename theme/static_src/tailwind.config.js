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

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

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
            green: {
                light: '#8cb18b',
                lightHover: '#8cc19b',
                base: '#588157',
                dark: '#2c402b',
                hover: '#3d583b'
            },
            
            smoke: {
                light: '#f5f5f5',
                base: '#ededed',
                dark: '#999999',
                
            },
            black: {
                100: '#0001',
                200: '#0002',
                300: '#0003',
                400: '#0004',
                500: '#0005',
                600: '#0006',
                700: '#0007',
                800: '#0008',
                900: '#0009',
                
            },
            white: {
                100: '#fff1',
                200: '#fff2',
                300: '#fff3',
                400: '#fff4',
                500: '#fff5',
                600: '#fff6',
                700: '#fff7',
                800: '#fff8',
                900: '#fff9',
            },

           blue: {
                light: '#264df7',
                base: '#072ac5',
                dark: '#041976',
           },
           red: {
                light: '#ed341d',
                base: '#941b0c',
                dark: '#76160a',
            },
            
            teste: {
                '--color-1': '#867832',
                2: 'red',
                3: '#abbbaa',
                4: 'yellow',
                5: 'pink',
                6: 'orange',
                
            }
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
