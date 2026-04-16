param(
    [Parameter(Mandatory=$true)]
    [string]$SourceDir,

    [switch]$RenameSequential,
    [switch]$CommitAndPush
)

$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot
$destDir = Join-Path $repoRoot 'atcoder\apg4b\answers'

if (-not (Test-Path $SourceDir)) {
    throw "Source directory not found: $SourceDir"
}

if (-not (Test-Path $destDir)) {
    throw "Destination directory not found: $destDir"
}

$files = Get-ChildItem -Path $SourceDir -File -Filter '*.py' | Sort-Object Name
if ($files.Count -eq 0) {
    throw 'No .py files found in source directory.'
}

if ($RenameSequential) {
    $index = 1
    foreach ($file in $files) {
        $targetName = ('q{0:D3}.py' -f $index)
        $targetPath = Join-Path $destDir $targetName
        Copy-Item -Path $file.FullName -Destination $targetPath -Force
        $index++
    }
} else {
    foreach ($file in $files) {
        $targetPath = Join-Path $destDir $file.Name
        Copy-Item -Path $file.FullName -Destination $targetPath -Force
    }
}

Write-Host "Imported $($files.Count) file(s) to $destDir"

if ($CommitAndPush) {
    Push-Location $repoRoot
    try {
        git add atcoder/apg4b/answers
        git status --short
        git commit -m ("apg4b: add {0} solutions" -f $files.Count)
        git push origin main
    }
    finally {
        Pop-Location
    }
}
