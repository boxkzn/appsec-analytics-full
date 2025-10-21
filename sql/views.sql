CREATE OR REPLACE VIEW v_open_counts AS
SELECT severity, COUNT(*) AS cnt
FROM vulns
WHERE fixed_at IS NULL
GROUP BY severity
ORDER BY severity;
