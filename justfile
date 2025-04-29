# Default command
default:
    @just --list --unsorted

run:
    @go run .

# Sync Go modules
tidy:
    go mod tidy
    go work sync
    @echo "All modules synced, Go workspace ready!"

# Run Pytest with arguments
test:
    go clean -testcache
    go test -cover ./...
