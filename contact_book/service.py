
def _norm_name(name):
    return name.strip().lower()


def _norm_phone(phone):
    return "".join(ch for ch in phone if ch.isdigit())


def _find(book, name):
    # Look up one contact by name (using the normalized comparison).
    # Returns the contact dict, or None if nobody matches.
    key = _norm_name(name)
    for c in book:
        if _norm_name(c["name"]) == key:
            return c
    return None


def _check_unique(book, name, phone, ignore=None):
    for c in book:
        if c is ignore:
            continue
        if name is not None and _norm_name(c["name"]) == _norm_name(name):
            raise ValueError(f"Duplicate name: {name!r}")
        if phone is not None and _norm_phone(c["phone"]) == _norm_phone(phone):
            raise ValueError(f"Duplicate phone: {phone!r}")
   

def add_contact(book, contact):
    # Reject duplicates first; if either check fails, nothing is added.
    _check_unique(book, contact["name"], contact["phone"])
    # Make sure every contact has a tags list, even if none was given.
    contact.setdefault("tags", [])
    book.append(contact)
    return contact


def get_all(book):
    # Return a NEW list sorted by name (case-insensitive).
    # sorted() doesn't modify the original book.
    return sorted(book, key=lambda c: _norm_name(c["name"]))


def search(book, query):
    # Partial, case-insensitive match against the name OR any tag.
    # e.g. "wor" matches the name "Howard" and the tag "work".
    q = query.strip().lower()
    return [
        c for c in get_all(book) # get_all keeps results sorted by name
        if q in c["name"].lower() or any(q in t.lower() for t in c.get("tags", []))
    ]


def edit_contact(book, name, **changes):
    # **changes collects whatever keyword arguments were passed, e.g.
    # edit_contact(book, "Bob", phone="555-0200") -> changes = {"phone": "555-0200"}
    contact = _find(book, name)
    if contact is None:
        raise KeyError(f"No contact named {name!r}")
    # Only check the fields being changed (.get gives None if not passed,
    # which _check_unique treats as "skip"). ignore=contact stops a contact
    # from clashing with itself, e.g. re-saving its own phone number.
    _check_unique(book, changes.get("name"), changes.get("phone"), ignore=contact)
    # dict.update only overwrites the given keys; other fields stay as-is.
    contact.update(changes)
    return contact


def delete_contact(book, name):
    contact = _find(book, name)
    if contact is None:
        raise KeyError(f"No contact named {name!r}")
    book.remove(contact)
    return contact # hand back the deleted contact, as the spec requires


def filter_by_tag(book, tag):
    # Unlike search(), this needs an EXACT tag match (still case-insensitive).
    # `t in (generator)` checks whether the tag appears among the contact's tags.
    t = tag.strip().lower()
    return [c for c in get_all(book) if t in (x.lower() for x in c.get("tags", []))]


if __name__ == "__main__":
    book = []
    add_contact(book, {"name": "Alice", "phone": "555-0101", "tags": ["work"]})
    add_contact(book, {"name": "Bob", "phone": "555-0102", "tags": ["friend"]})
    try:
        # Same name as Alice (different case) -> should be rejected
        add_contact(book, {"name": "alice", "phone": "555-0199"})
    except ValueError as e:
        print("Rejected:", e)
    print([c["name"] for c in search(book, "wor")]) # ['Alice']
    edit_contact(book, "bob", phone="555-0200") # only phone changes
    print([c["name"] for c in filter_by_tag(book, "FRIEND")]) # ['Bob']
    print(delete_contact(book, "Alice")) # prints the removed dict
