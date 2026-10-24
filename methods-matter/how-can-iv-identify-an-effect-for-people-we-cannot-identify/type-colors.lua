-- Render-time typography only. The author's editable words remain unchanged.
-- Match full singular/plural type names, preserving case and punctuation.
local forms = {
  {"complier", "type-complier"}, {"compliers", "type-complier"},
  {"always-taker", "type-always-taker"}, {"always-takers", "type-always-taker"},
  {"never-taker", "type-never-taker"}, {"never-takers", "type-never-taker"},
  {"defier", "type-defier"}, {"defiers", "type-defier"}
}

local function whole_word(text, first, last)
  local before = first > 1 and text:sub(first - 1, first - 1) or ""
  local after = last < #text and text:sub(last + 1, last + 1) or ""
  return not before:match("[A-Za-z0-9_]") and not after:match("[A-Za-z0-9_]")
end

function Str(element)
  local original, lower = element.text, element.text:lower()
  local cursor, changed = 1, false
  local result = pandoc.List()
  while cursor <= #original do
    local first, last, class
    for _, form in ipairs(forms) do
      local search = cursor
      while search <= #lower do
        local a, b = lower:find(form[1], search, true)
        if not a then break end
        if whole_word(lower, a, b) then
          if not first or a < first or (a == first and b > last) then
            first, last, class = a, b, form[2]
          end
          break
        end
        search = a + 1
      end
    end
    if not first then
      result:insert(pandoc.Str(original:sub(cursor)))
      break
    end
    if first > cursor then result:insert(pandoc.Str(original:sub(cursor, first - 1))) end
    result:insert(pandoc.Span(pandoc.Str(original:sub(first, last)),
      pandoc.Attr("", {"compliance-type", class})))
    changed = true
    cursor = last + 1
  end
  if changed then return result end
end
