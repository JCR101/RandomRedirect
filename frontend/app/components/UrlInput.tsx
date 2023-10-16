export default function UrlInput({ index }: { index: number }) {
  const numberToOrdinal = (number: number): string => {
    if (number < 0 || number > 1000) {
      return "Number out of range (0-1000)";
    }

    if (number === 0) return "zero";

    const onesCardinal = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    const tensCardinal = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'];
    const onesOrdinal = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth'];
    const teensOrdinal = ['eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth'];
    const tensOrdinal = ['', 'tenth', 'twentieth', 'thirtieth', 'fortieth', 'fiftieth', 'sixtieth', 'seventieth', 'eightieth', 'ninetieth'];

    if (number === 1000) return 'one-thousandth'

    if (number % 100 === 0) return `${onesCardinal[Math.floor(number / 100)]}-hundredth`

    if (number > 100) return `${onesCardinal[Math.floor(number / 100)]}-hundred and ${numberToOrdinal(number - (Math.floor(number / 100) * 100))}`

    if (number % 10 === 0) return tensOrdinal[Math.floor(number / 10)];

    if (number < 10) return onesOrdinal[number - 1];

    if (number >= 11 && number <= 19) return teensOrdinal[number - 11];

    return `${tensCardinal[Math.floor(number / 10)]}-${onesOrdinal[number % 10 - 1]}`;
  }

  return (
    <div>
      <div className="w-full items-center flex flex-col mb-8">
        <div className="max-w-xl w-full">
          <div className="font-black ml-4 mb-0">{numberToOrdinal(index)} url</div>
        </div>
        <input className="max-w-xl w-full font-bold shadow-hard bg-background-light text-foreground rounded-tl-2xl rounded-br-2xl p-2" />
      </div>
    </div>
  )
}
