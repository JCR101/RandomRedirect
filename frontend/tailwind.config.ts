import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    colors: {
      'foreground': '#ECECEC',
      'background': '#352D39',
      'background-dark': '#2B252E',
      'background-light': '#4D4452'
    },
    extend: {
      boxShadow: {
        'hard': '10px 10px 0px 0px rgba(0, 0, 0, 0.25)'
      },
      rounded: {
        'tlbr': '1.25rem 0rem'
      }
    }
  },
  plugins: [],
}
export default config
