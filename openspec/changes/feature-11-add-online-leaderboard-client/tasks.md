## 1. Client Boundary

- [ ] 1.1 Define leaderboard client interface for submit and top-record fetch.
- [ ] 1.2 Implement configurable remote URL resolution.
- [ ] 1.3 Implement local fallback composition with existing local leaderboard storage.

## 2. HTTP Behavior

- [ ] 2.1 Implement score submission with timeout and error handling.
- [ ] 2.2 Implement top-score fetch with timeout and invalid-response handling.
- [ ] 2.3 Add logging or status reporting for remote failures without UI interruption.

## 3. Tests

- [ ] 3.1 Add tests for disabled remote mode.
- [ ] 3.2 Add tests for successful submit and fetch using mocked HTTP.
- [ ] 3.3 Add tests for timeout, connection error, and invalid response fallback.
