$f = 'c:\Users\priest\Desktop\rerenwangzhan\index.html'
$c = [System.IO.File]::ReadAllText($f, [System.Text.Encoding]::UTF8)

# Find the works section
$startIdx = $c.IndexOf('<section class="section works"')
$endIdx = $c.IndexOf('</section><section class="section stage', $startIdx)

if ($startIdx -ge 0 -and $endIdx -ge 0) {
    $worksSection = $c.Substring($startIdx, $endIdx - $startIdx)
    # Show the section content
    Write-Output "=== WORKS SECTION ==="
    Write-Output $worksSection.Substring(0, [Math]::Min(500, $worksSection.Length))
    Write-Output "..."
} else {
    Write-Output "Works section not found"
}
