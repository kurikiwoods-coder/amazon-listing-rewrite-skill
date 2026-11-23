"""Measure supplied Listing text exactly as provided, using caller-selected limits."""
import json
import sys


def measure(field):
    if not isinstance(field, dict) or not isinstance(field.get("field"), str) or not field["field"].strip():
        raise ValueError("Each entry needs a field name.")
    unit = field.get("unit", "characters")
    if unit not in ("characters", "utf8_bytes"):
        raise ValueError("unit must be characters or utf8_bytes.")
    limit = field.get("limit")
    if limit is not None and (type(limit) is not int or limit < 0):
        raise ValueError("limit must be a nonnegative integer.")
    op = field.get("op", "<=")
    if op not in ("<", "<="):
        raise ValueError("op must be < or <=.")
    result = {"field": field["field"], "unit": unit, "limit": limit, "op": op}
    for version in ("before", "after"):
        value = field.get(version)
        if value is not None and not isinstance(value, str):
            raise ValueError(f"{version} must be a string or null.")
        if value is None:
            result[version] = {"length": None, "status": "not_provided"}
            continue
        length = len(value.encode("utf-8")) if unit == "utf8_bytes" else len(value)
        status = "rule_unknown"
        if limit is not None:
            within_limit = length < limit if op == "<" else length <= limit
            status = "within_limit" if within_limit else "over_limit"
        result[version] = {"length": length, "status": status}
    return result


def main():
    try:
        fields = json.load(sys.stdin)
        if not isinstance(fields, list):
            raise ValueError("Expected a JSON list of field entries.")
        results = [measure(field) for field in fields]
    except (ValueError, UnicodeError) as exc:
        print(f"Invalid input: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
