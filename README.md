# numeric_constant_traits

Traits for generic numeric constants

Like the traits `Zero` and `One` from the `num` crate, but for all natural
numbers up to and including 100. Allows doing generic arithmetic without
having to do casts.

Without this crate you'd need to do something like:
```ignore
2u8.into() * 3u8.into() + 4u8.into()
```
Which is okay, but obfuscates a bit what the intent is.

With this crate you can do something like this:
```ignore
T::two() * T::three() + T::four()
```

The traits are implemented for all standard numeric types, as well as a blanket
implementation for `num::Complex<T>`, where `T` is any of the standar numeric
types.
