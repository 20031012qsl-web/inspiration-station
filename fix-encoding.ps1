# Read the file as raw bytes
$f = 'c:\Users\priest\Desktop\rerenwangzhan\index.html'
$bytes = [System.IO.File]::ReadAllBytes($f)

# Try to decode as GBK (the garbled text is UTF-8 bytes interpreted as GBK)
$gbk = [System.Text.Encoding]::GetEncoding('GBK')
$content = $gbk.GetString($bytes)

# Check if we got proper Chinese now
if ($content -match '多维视觉') {
    Write-Output "Successfully decoded with GBK!"
    # Now save as UTF-8 without BOM
    $utf8NoBom = New-Object System.Text.UTF8Encoding $false
    [System.IO.File]::WriteAllText($f, $content, $utf8NoBom)
    Write-Output "Saved as UTF-8 without BOM"
} else {
    Write-Output "GBK decoding didn't work, trying other approaches..."
    Write-Output "First 100 chars: $($content.Substring(0, [Math]::Min(100, $content.Length)))"
}
