import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './app/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        dark: '#0F172A',
        surface: '#1E293B',
      },
    },
  },
  plugins: [],
  darkMode: 'class',
}
export default config
