func solution(s string) string {
	middle := len(s) % 2
	length := len(s) / 2
	
	if middle == 1 {
			return s[length : length + 1]
	}
	
	return s[length - 1 : length + 1]
}