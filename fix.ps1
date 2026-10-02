$content = [System.IO.File]::ReadAllText('C:\Users\Giordano\Documents\GitHub\portfolio\rewild.html', [System.Text.Encoding]::UTF8)
$content = $content.Replace('identit', 'identità').Replace('qualit', 'qualità').Replace('socialit', 'socialità').Replace('Pubblicit', 'Pubblicità')
[System.IO.File]::WriteAllText('C:\Users\Giordano\Documents\GitHub\portfolio\rewild.html', $content, [System.Text.Encoding]::UTF8)
