import type { ReactNode } from 'react'

export default function RootLayout({
  children,
}: {
  children: ReactNode
}) {
  return (
    <html lang="pt">
      <body className="bg-dark text-white">
        {children}
      </body>
    </html>
  )
}
