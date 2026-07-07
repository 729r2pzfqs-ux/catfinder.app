/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./**/*.html'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        display: ['Instrument Serif', 'Georgia', 'serif']
      },
      colors: {
        cream: {
          50: '#faf9f6',
          100: '#f7f6f2',
          200: '#f3f0ec',
          300: '#edeae5',
          400: '#dcd9d5',
        },
        teal: {
          50: '#eef8f8',
          100: '#d5eded',
          200: '#aadada',
          300: '#6fbfc0',
          400: '#3da0a3',
          500: '#01696f',
          600: '#0c4e54',
          700: '#0f3638',
        }
      }
    }
  },
  plugins: [],
}
