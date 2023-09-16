# Statement 1: The system is in multiuser state if and only if it is operating normally.
function Statement1($multiuser, $operatingNormally) {
    return ($multiuser -eq $operatingNormally)
}

# Statement 2: If the system is operating normally, the kernel is functioning.
function Statement2($operatingNormally, $kernelFunctioning) {
    return (-not $operatingNormally -or $kernelFunctioning)
}

# Statement 3: The kernel is not functioning or the system is in interrupt mode.
function Statement3($kernelFunctioning, $interruptMode) {
    return (-not $kernelFunctioning -or $interruptMode)
}

# Statement 4: If the system is not in multiuser state, then it is in interrupt mode.
function Statement4($multiuser, $interruptMode) {
    return (-not $multiuser -or $interruptMode)
}

# Statement 5: The system is not in interrupt mode.
function Statement5($interruptMode) {
    return (-not $interruptMode)
}

# Check consistency
$multiuser = $true
$operatingNormally = $true
$kernelFunctioning = $true
$interruptMode = $false

# Check if all statements are consistent
$consistent = Statement1 $multiuser $operatingNormally `
              -and Statement2 $operatingNormally $kernelFunctioning `
              -and Statement3 $kernelFunctioning $interruptMode `
              -and Statement4 $multiuser $interruptMode `
              -and Statement5 $interruptMode

if ($consistent) {
    Write-Output "The system specifications are consistent."
} else {
    Write-Output "The system specifications are not consistent."
}
