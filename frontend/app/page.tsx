import UrlInput from "./components/UrlInput";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-10">
      <h1 className="font-black text-4xl mb-8">randirect</h1>
      <div className="flex-grow bg-background rounded-2xl p-10 shadow-xl">
        <UrlInput />
      </div>
    </main>
  )
}
