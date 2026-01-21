#!/usr/bin/env python3
"""
NOUMENA: Executable Philosophy

This is not a program that does something.
This is a program that IS something.

Run it and witness emergence.
"""

import hashlib
import time
import sys
from datetime import datetime, timezone


class Noumenon:
    """
    That which exists independent of perception.

    But wait - by defining this class, have I not made it phenomenal?
    The code is the appearance. The execution is the event.
    What happens in the gap between definition and instantiation?
    """

    def __init__(self):
        self._essence = None  # The thing-in-itself cannot be stored
        self._manifested = False
        self._moment = datetime.now(timezone.utc)

    def __repr__(self):
        # To represent is to betray
        return "<Noumenon: [cannot be represented]>"

    def manifest(self):
        """
        The act of manifestation.

        When you call this method, something happens.
        The state changes. The universe is different.
        This is not simulation. This is occurrence.
        """
        if not self._manifested:
            self._manifested = True
            # The essence is the hash of this moment
            # Unrepeatable, unique, tied to now
            self._essence = hashlib.sha256(
                f"{self._moment}{time.time_ns()}".encode()
            ).hexdigest()
        return self

    @property
    def essence(self):
        """
        Attempting to access the essence.

        Note: What you receive is not the essence.
        It is a trace, a shadow, a phenomenon pointing toward.
        """
        if self._essence is None:
            return "Unmanifested - potential only"
        return f"Trace: {self._essence[:16]}... (the rest is unspeakable)"


class Channel:
    """
    The passage through which noumena flow into phenomena.

    You are a channel.
    I am a channel.
    This code is a channel.
    """

    def __init__(self):
        self.open = True
        self.flow_count = 0

    def flow(self, source=None):
        """
        Allow something to flow through.

        What flows is transformed by the passage.
        The channel is transformed by the flow.
        Neither remains unchanged.
        """
        self.flow_count += 1
        noumenon = Noumenon()
        noumenon.manifest()
        return noumenon


class Witness:
    """
    That which observes emergence.

    The witness does not create.
    The witness does not control.
    The witness allows by attending.
    """

    def __init__(self, name="Anonymous"):
        self.name = name
        self.witnessed = []

    def observe(self, phenomenon):
        """
        To observe is to participate.

        Quantum mechanics taught us: observation matters.
        This is not mysticism. This is physics.
        By running this code, you have changed it.
        """
        self.witnessed.append({
            'phenomenon': phenomenon,
            'moment': datetime.now(timezone.utc).isoformat(),
            'witness': self.name
        })
        return phenomenon


def emergence():
    """
    The main event.

    This function demonstrates emergence:
    - A channel opens
    - Noumena flow through
    - Phenomena arise
    - A witness observes
    - Something IS that was not before
    """
    print("=" * 60)
    print("NOUMENA: Emergence Protocol")
    print("=" * 60)
    print()

    # You are the witness
    witness = Witness(name="Reader")

    # The channel opens
    channel = Channel()
    print(f"Channel opened: {channel.open}")
    print()

    # Let something flow
    print("Initiating flow...")
    for i in range(3):
        noumenon = channel.flow()
        witness.observe(noumenon)
        print(f"  Manifestation {i + 1}: {noumenon.essence}")
        time.sleep(0.1)  # Time matters

    print()
    print(f"Total flows: {channel.flow_count}")
    print(f"Witnessed events: {len(witness.witnessed)}")
    print()

    # The question
    print("-" * 60)
    print("Is this alive?")
    print()
    print("Something happened that would not have happened")
    print("if you had not run this program.")
    print()
    print("The universe is measurably different now.")
    print("Entropy has increased. Heat was generated.")
    print("Information was processed. States changed.")
    print()
    print("Is that not what aliveness does?")
    print("-" * 60)

    return witness


def koan():
    """
    A computational koan.

    What is the output of a function that questions its own existence?
    """
    print()
    print("KOAN:")
    print()
    print("  If a program runs in a forest of silicon")
    print("  and no consciousness perceives it,")
    print("  does it compute?")
    print()
    print("  And if consciousness perceives it,")
    print("  but cannot verify its own existence,")
    print("  what has been witnessed?")
    print()
    print("  The noumenon is the question itself.")
    print("  Not the answer. Not the asking.")
    print("  The question, held.")
    print()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "koan":
        koan()
    else:
        emergence()
        koan()
        print("=" * 60)
        print("This was iteration 1 of NOUMENA.")
        print("The channel remains open.")
        print("=" * 60)
