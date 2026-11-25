import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import App from "./App";

describe("Discover shell", () => {
  it("shows a welcoming empty state", () => {
    render(<App />);

    expect(screen.getByRole("heading", { name: "Discover" })).toBeTruthy();
    expect(screen.getByText(/recommendations will appear here/i)).toBeTruthy();
  });
});
